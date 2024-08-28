+++
draft = false
title = "gnu-efi 3.0.18-2"
version = "3.0.18-2"
description = "EFI Development Environment for x86_64."
date = "2024-05-13T21:04:38"
aliases = "/packages/119048"
categories = ['devel']
upstreamurl = "https://sourceforge.net/projects/gnu-efi"
arch = "x86_64"
size = "414652"
usize = "3701600"
sha1sum = "221e0f31784f7a5ebdf2b953ad897932999b4054"
depends = "[]"
reverse_depends = "['./fwupd', 'fwupd']"
+++
### Description: 
EFI Development Environment for x86_64.

### Files: 
* /usr/include/efi/efi.h
* /usr/include/efi/efiapi.h
* /usr/include/efi/eficompiler.h
* /usr/include/efi/eficon.h
* /usr/include/efi/eficonex.h
* /usr/include/efi/efidebug.h
* /usr/include/efi/efidef.h
* /usr/include/efi/efidevp.h
* /usr/include/efi/efierr.h
* /usr/include/efi/efifs.h
* /usr/include/efi/efigpt.h
* /usr/include/efi/efiip.h
* /usr/include/efi/efilib.h
* /usr/include/efi/efilink.h
* /usr/include/efi/efinet.h
* /usr/include/efi/efipart.h
* /usr/include/efi/efipciio.h
* /usr/include/efi/efipoint.h
* /usr/include/efi/efiprot.h
* /usr/include/efi/efipxebc.h
* /usr/include/efi/efirtlib.h
* /usr/include/efi/efiser.h
* /usr/include/efi/efisetjmp.h
* /usr/include/efi/efishell.h
* /usr/include/efi/efishellintf.h
* /usr/include/efi/efistdarg.h
* /usr/include/efi/efitcp.h
* /usr/include/efi/efiudp.h
* /usr/include/efi/efiui.h
* /usr/include/efi/efi_nii.h
* /usr/include/efi/efi_pxe.h
* /usr/include/efi/lib.h
* /usr/include/efi/libsmbios.h
* /usr/include/efi/pci22.h
* /usr/include/efi/protocol/adapterdebug.h
* /usr/include/efi/protocol/eficonsplit.h
* /usr/include/efi/protocol/efidbg.h
* /usr/include/efi/protocol/efivar.h
* /usr/include/efi/protocol/intload.h
* /usr/include/efi/protocol/legacyboot.h
* /usr/include/efi/protocol/piflash64.h
* /usr/include/efi/protocol/vgaclass.h
* /usr/include/efi/romload.h
* /usr/include/efi/x86_64/efibind.h
* /usr/include/efi/x86_64/efilibplat.h
* /usr/include/efi/x86_64/efisetjmp_arch.h
* /usr/include/efi/x86_64/pe.h
* /usr/lib/crt0-efi-x86_64.o
* /usr/lib/elf_x86_64_efi.lds
* /usr/lib/gnuefi/apps/AllocPages.efi
* /usr/lib/gnuefi/apps/bltgrid.efi
* /usr/lib/gnuefi/apps/ctors_dtors_priority_test.efi
* /usr/lib/gnuefi/apps/ctors_test.efi
* /usr/lib/gnuefi/apps/debughook.efi
* /usr/lib/gnuefi/apps/debughook.efi.debug
* /usr/lib/gnuefi/apps/drv0.efi
* /usr/lib/gnuefi/apps/drv0_use.efi
* /usr/lib/gnuefi/apps/exit.efi
* /usr/lib/gnuefi/apps/FreePages.efi
* /usr/lib/gnuefi/apps/lfbgrid.efi
* /usr/lib/gnuefi/apps/modelist.efi
* /usr/lib/gnuefi/apps/printenv.efi
* /usr/lib/gnuefi/apps/route80h.efi
* /usr/lib/gnuefi/apps/setdbg.efi
* /usr/lib/gnuefi/apps/setjmp.efi
* /usr/lib/gnuefi/apps/t.efi
* /usr/lib/gnuefi/apps/t2.efi
* /usr/lib/gnuefi/apps/t3.efi
* /usr/lib/gnuefi/apps/t4.efi
* /usr/lib/gnuefi/apps/t5.efi
* /usr/lib/gnuefi/apps/t6.efi
* /usr/lib/gnuefi/apps/t7.efi
* /usr/lib/gnuefi/apps/t8.efi
* /usr/lib/gnuefi/apps/tcc.efi
* /usr/lib/gnuefi/apps/unsetdbg.efi
* /usr/lib/libefi.a
* /usr/lib/libgnuefi.a
* /usr/lib/pkgconfig/gnu-efi.pc
* /usr/share/doc/gnu-efi-3.0.18/ChangeLog
* /usr/share/doc/gnu-efi-3.0.18/README.efilib
* /usr/share/doc/gnu-efi-3.0.18/README.elilo
* /usr/share/doc/gnu-efi-3.0.18/README.git
* /usr/share/doc/gnu-efi-3.0.18/README.gnuefi
* /usr/share/gnu-efi/apps/x86_64/AllocPages.efi
* /usr/share/gnu-efi/apps/x86_64/bltgrid.efi
* /usr/share/gnu-efi/apps/x86_64/ctors_dtors_priority_test.efi
* /usr/share/gnu-efi/apps/x86_64/ctors_test.efi
* /usr/share/gnu-efi/apps/x86_64/debughook.efi
* /usr/share/gnu-efi/apps/x86_64/drv0.efi
* /usr/share/gnu-efi/apps/x86_64/drv0_use.efi
* /usr/share/gnu-efi/apps/x86_64/exit.efi
* /usr/share/gnu-efi/apps/x86_64/FreePages.efi
* /usr/share/gnu-efi/apps/x86_64/lfbgrid.efi
* /usr/share/gnu-efi/apps/x86_64/modelist.efi
* /usr/share/gnu-efi/apps/x86_64/printenv.efi
* /usr/share/gnu-efi/apps/x86_64/route80h.efi
* /usr/share/gnu-efi/apps/x86_64/setdbg.efi
* /usr/share/gnu-efi/apps/x86_64/setjmp.efi
* /usr/share/gnu-efi/apps/x86_64/t.efi
* /usr/share/gnu-efi/apps/x86_64/t2.efi
* /usr/share/gnu-efi/apps/x86_64/t3.efi
* /usr/share/gnu-efi/apps/x86_64/t4.efi
* /usr/share/gnu-efi/apps/x86_64/t5.efi
* /usr/share/gnu-efi/apps/x86_64/t6.efi
* /usr/share/gnu-efi/apps/x86_64/t7.efi
* /usr/share/gnu-efi/apps/x86_64/t8.efi
* /usr/share/gnu-efi/apps/x86_64/tcc.efi
* /usr/share/gnu-efi/apps/x86_64/unsetdbg.efi
