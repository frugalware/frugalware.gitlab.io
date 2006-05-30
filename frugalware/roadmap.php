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
 * Frugalware Linux Homepage - About (summary) page
 *
 * @author Krisztian VASAS <iron@frugalware.org>
 * @author Miklos Vajna <vmiklos@frugalware.org>
 *
 * @copyright Copyright (c) 2006. Krisztian VASAS
 * @copyright Copyright (c) 2005-2006. Miklos Vajna
 */

// include some useful functions
include("functions.inc.php");

$lang = getlang();
$llang = getllang($lang);
$aboutfile = "includes/about.".$lang.".php";

// set the locale settings for gettext
putenv("LANG=".$llang);
setlocale(LC_ALL,$llang);
$domain = 'messages';
bindtextdomain($domain, "locale");
textdomain($domain);

// include the config and let's start page
include("config.inc.php");
include("header.php");

?>

<!-- main content start -->
<div id="columns">
	<div id="leftcolumn">
<?php
fwsidebox(gettext("Menu"), $menucontent);
fwsidebox(gettext("Languages"), $langcontent);
?>
	</div>

	<div id="rightcolumn">
<?php
fwsidebox(gettext("Information"), $validcontent);
?>
	</div>

	<div id="centercolumn">
<?php

fwmiddlebox("0.5 (<acronym title=\"A planet prominent in Foundation and Foundation and Empire.\">Siwenna</acronym>)",
"<table width=\"100%\">
<tr><td>Sep 30, 2006<td>0.5<td><i>pending</i>
<tr><td>Aug 31, 2006<td>0.5rc2<td><i>pending</i>
<tr><td>Aug 17, 2006<td>0.5rc1<td><i>pending</i>
<tr><td>Jul 20, 2006<td>0.5pre2<td><i>pending</i>
<tr><td width=\"30%\">May 25, 2006<td width=\"30%\">0.5pre1<td width=\"30%\"><i>done</i>
</table>
");

fwmiddlebox("0.4 (<acronym title=\"The temporary headquarters for the navy of Bel Riose, during the war between the Empire and the Foundation.\">Wanda</acronym>)",
"<table width=\"100%\">
<tr><td>Mar 30, 2006<td>0.4<td><i>done</i>
<tr><td>Mar 16, 2006<td>0.4rc2<td><i>done</i>
<tr><td>Mar 2, 2006<td>0.4rc1<td><i>done</i>
<tr><td>Feb 2, 2006<td>0.4pre2<td><i>done</i>
<tr><td width=\"30%\">Dec 8, 2005<td width=\"30%\">0.4pre1<td width=\"30%\"><i>done</i>
</table>
");

fwmiddlebox("0.3 (<acronym title=\"a fictional planet in Isaac Asimov's Foundation series and Empire series of science-fiction novels\">Trantor</acronym>)",
"<table width=\"100%\">
<tr><td>Oct 13, 2005<td>0.3<td><i>done</i>
<tr><td>Oct 4, 2005<td>0.3rc2<td><i>done</i>
<tr><td>Sep 16, 2005<td>0.3rc1<td><i>done</i>
<tr><td>Aug 18, 2005<td>0.3pre2<td><i>done</i>
<tr><td width=\"30%\">Jun 23, 2005<td width=\"30%\">0.3pre1<td width=\"30%\"><i>done</i>
</table>
");

fwmiddlebox("0.2 (<acronym title=\"a fictional planet in Isaac Asimov's Robot Series\">Aurora</acronym>)",
"<table width=\"100%\">
<tr><td>Apr 28, 2005<td>0.2<td><i>done</i>
<tr><td>Apr 18, 2005<td>0.2rc2<td><i>done</i>
<tr><td>Apr 7, 2005<td>0.2rc1<td><i>done</i>
<tr><td>Feb 24, 2005<td>0.2pre2<td><i>done</i>
<tr><td width=\"30%\">Jan 10, 2005<td width=\"30%\">0.2pre1<td width=\"30%\"><i>done</i>
</table>
");

fwmiddlebox("0.1 (<acronym title=\"the first book of the Hebrew Bible\">Genesis</acronym>)",
"<table width=\"100%\">
<tr><td>Nov  2, 2004<td>0.1<td><i>done</i>
<tr><td>Oct 11, 2004<td>0.1rc2<td><i>done</i>
<tr><td width=\"30%\">Sep 29, 2004<td width=\"30%\">0.1rc1<td width=\"30%\"><i>done</i>
</table>
");
?>
	</div>
</div>
<!-- main content end -->

<?php
include("footer.php");
?>
