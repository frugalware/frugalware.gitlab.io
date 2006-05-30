<?php

/**
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License v2 as published by
 the Free Software Foundation

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
 GNU General Public License for more details.
 */

/**
 * Frugalware Linux Homepage - RSS feed
 *
 * @author Miklos Vajna <vmiklos@frugalware.org>
 * @author Krisztian VASAS <iron@frugalware.org>
 * @copyright Copyright (c) 2006. Krisztian VASAS
 */

include("config.inc.php");
include("functions.inc.php");
include("db.inc.php");

switch($_GET['type'])
{
	case "stable":
		$db = new FwDB();
		$db->doConnect($sqlhost, $sqluser, $sqlpass, "frugalware");

		$handle['title']="Frugalware Linux";
		$handle['desc']="Frugalware Linux is general purpose Linux distribution designed for intermediate users. Some of its elements were borrowed from Slackware Linux and Arch Linux.";
		$handle['link']="http://frugalware.org/";
		$query="select version, `desc` from releases where type='stable' order by date desc";
		$result = $db->doQuery($query);
		while ($i = $db->doFetchRow($result))
		{
			$handle['items'][] = array(
				"title" => "frugalware-" . $i['version'],
				"desc" => $i['desc'],
				"link" => "http://frugalware.org/download.php?url=frugalware-" . $i['version'] . "-iso/frugalware-" . $i['version'] . "-dvd.iso"
			);
		}
		$db->doClose();
		break;

	case "packages":
		$db  = new FwDB();
		$db->doConnect($sqlhost, $sqluser, $sqlpass, "frugalware");

		$handle['title']="Frugalware Linux Packages";
		$handle['desc']="Latest updates to the Frugalware Linux package repositories.";
		$handle['link']="http://frugalware.org/packages.php";
		$query="select groups, pkgname, id, pkgver, pkgrel, arch, `desc`, unix_timestamp(updated), uploader from packages order by updated desc limit 10";
		$result = $db->doQuery($query);
		while ($i = $db->doFetchRow($result))
		{
			$handle['items'][] = array(
				"title" => preg_replace("/^([^ ]*) .*/", "$1", $i['groups']) . "/${i['pkgname']}-${i['pkgver']}-${i['pkgrel']}-${i['arch']}",
				"desc" => $i['desc'],
				"author" => $i['uploader'],
				"pubDate" => date(DATE_RFC2822, $i['unix_timestamp(updated)']),
				"link" => "http://frugalware.org/packages.php?id=${i['id']}"
			);
		}
		$db->doClose();
		break;

	case "darcs":
		header('Content-Type: application/xml; charset=utf-8');
		print(file_get_contents("http://darcs.frugalware.org/genesis.darcsweb/darcsweb.cgi?r=frugalware-current;a=rss"));
		die();
	case "bugs":
		header('Content-Type: application/xml; charset=utf-8');
		print(file_get_contents("http://bugs.frugalware.org/rss.php?type=new"));
		die();
	case "blogs":
		header('Content-Type: application/xml; charset=utf-8');
		print(file_get_contents("http://blogs.frugalware.org/xmlsrv/rss2.php?blog=1"));
		die();
	default:
		include("header.php");
		fwmiddlebox("RSS",'<div align="left"><ul>
			<li><a href="/rss.php?type=stable">Stable releases</a></li>
			<li><a href="/rss.php?type=darcs">Darcs commits</a></li>
			<li><a href="/rss.php?type=bugs">BTS entries</a></li>
			<li><a href="/rss.php?type=packages">Package updates</a></li>
			<li><a href="/rss.php?type=blogs">Blog posts</a></li>
			</ul></div>'
		);
		include("footer.php");
		die();
}
header('Content-Type: application/xml; charset=utf-8');
print("<?xml version=\"1.0\" encoding=\"utf-8\"?>
<rss version=\"2.0\">
<channel>
	<title>".$handle['title']."</title>
	<description>".$handle['desc']."</description>
	<link>".$handle['link']."</link>\n"
);
foreach( $handle['items'] as $i )
{
	print("<item>\n<title>".$i['title']."</title>\n<description>".htmlspecialchars($i['desc'])."</description>\n<link>".$i['link']."</link>\n");
	if(isset($i['author']))
	{
		print("<author>".$i['author']."</author>\n");
	}
	if(isset($i['pubDate']))
	{
		print("<pubDate>".$i['pubDate']."</pubDate>\n");
	}
	print("</item>\n");
}
print("</channel>\n</rss>");
?>
