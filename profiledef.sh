#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="archlinux-baseline"
iso_label="inxi-collect_$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y%m)"
iso_publisher="TerminalHermit"
iso_application="Arch Linux baseline"
iso_version="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito'
           'uefi-ia32.grub.esp' 'uefi-x64.grub.esp'
           'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="erofs"
airootfs_image_tool_options=('-zlz4' -E 'ztailpacking,fragments,dedupe')
bootstrap_tarball_compression=(zstd -c -T$(nproc) --long -15)
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root/script"]="0:0:770"
  ["/root/.bash_profile"]="0:0:770"
)
