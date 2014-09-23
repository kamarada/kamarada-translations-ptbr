#
# spec file for package kamarada-translations-ptbr
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define language pt_BR
%define version 13.1

Name:           kamarada-translations-ptbr
Version:        %{version}
Release:        1
Summary:        Brazilian Portuguese translations to Kamarada %{version}
License:        GPL-2.0+
Group:          System/Localization
Source0:        LICENSE
Url:            http://github.com/kamarada/kamarada-translations-ptbr
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  apparmor-utils-lang
BuildRequires:  apper-lang
BuildRequires:  bluedevil-lang
BuildRequires:  cups-pk-helper-lang
# BuildRequires:  glibc-locale TODO ?
BuildRequires:  kamoso-lang
BuildRequires:  libpurple-lang
BuildRequires:  libpurple-plugin-skype-lang
BuildRequires:  MozillaFirefox-translations-common
BuildRequires:  skanlite-lang
BuildRequires:  vlc-noX-lang
BuildRequires:  yakuake-lang

BuildRequires:  bluez
BuildRequires:  libswscale2

Conflicts:      otherproviders(apparmor-utils-lang)
Conflicts:      otherproviders(apper-lang)
Conflicts:      otherproviders(bluedevil-lang)
Conflicts:      otherproviders(cups-pk-helper-lang)
Conflicts:      otherproviders(kamoso-lang)
Conflicts:      otherproviders(libpurple-lang)
Conflicts:      otherproviders(libpurple-plugin-skype-lang)
Conflicts:      otherproviders(MozillaFirefox-translations-common)
Conflicts:      otherproviders(skanlite-lang)
Conflicts:      otherproviders(vlc-noX-lang)
Conflicts:      otherproviders(yakuake-lang)

Provides:       apparmor-utils-lang
Provides:       apper-lang
Provides:       bluedevil-lang
Provides:       cups-pk-helper-lang
Provides:       kamoso-lang
Provides:       libpurple-lang
Provides:       libpurple-plugin-skype-lang
Provides:       MozillaFirefox-translations-common
Provides:       skanlite-lang
Provides:       vlc-noX-lang
Provides:       yakuake-lang

Requires:       bundle-lang-common-pt
Requires:       bundle-lang-kde-pt
Requires:       kde4-l10n-pt_BR
Requires:       kde4-l10n-pt_BR-data
Requires:       libreoffice-l10n-pt-BR
Requires:       libreoffice-thesaurus-pt
Requires:       translation-update-pt_BR
Requires:       yast2-trans-pt_BR


%description
Brazilian Portuguese translations to Kamarada %{version}


%prep
cp -a %{SOURCE0} COPYING


%build


%install
# Search for translations in packages
packages=""
packages="$packages apparmor-utils-lang"
packages="$packages apper-lang"
packages="$packages bluedevil-lang"
packages="$packages cups-pk-helper-lang"
packages="$packages kamoso-lang"
packages="$packages libpurple-lang"
packages="$packages libpurple-plugin-skype-lang"
# packages="$packages MozillaFirefox-translations-common"
packages="$packages skanlite-lang"
packages="$packages vlc-noX-lang"
packages="$packages yakuake-lang"

echo "" > files_to_add

for p in $packages; do
  rpm -q --qf '[%{FILENAMES}\n]' $p | grep %{language} | while read file; do
    echo "$file" >> files_to_add
  done
done

# Files from MozillaFirefox-translations-common
echo "/usr/lib/firefox/browser/extensions/langpack-pt-BR@firefox.mozilla.org/" >> files_to_add

# Add files to package
echo "%defattr(-,root,root)" > files.kamarada-translations-ptbr
echo "%doc COPYING" >> files.kamarada-translations-ptbr

for f in `cat files_to_add`; do
  if ! test -L "$f" && test -d "$f"; then
    mkdir -p $RPM_BUILD_ROOT/$f
    cp -R "$f/" "$RPM_BUILD_ROOT/$f/../"
  else
    mkdir -p $RPM_BUILD_ROOT/`dirname "$f"`
    cp -a "$f" "$RPM_BUILD_ROOT/$f"
  fi
  echo "$f" >> files.kamarada-translations-ptbr
done

rm files_to_add


%files -f files.kamarada-translations-ptbr


%changelog
* Fri Sep 12 2014 kamaradalinux@gmail.com
- Initial draft
