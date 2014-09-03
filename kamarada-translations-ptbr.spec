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


Name:           kamarada-translations-ptbr
Version:        13.1
Release:        1
Summary:        Brazilian Portuguese translations to Kamarada
License:        GPL-2.0+
Group:          System/Localization
Source0:        LICENSE
Url:            http://github.com/kamarada/kamarada-translations-ptbr
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  MozillaFirefox-translations-common

Conflicts:      otherproviders(MozillaFirefox-translations-common)

Provides:       MozillaFirefox-translations-common

Requires:       bundle-lang-common-pt
Requires:       kde4-l10n-pt_BR
Requires:       kde4-l10n-pt_BR-data
Requires:       libreoffice-l10n-pt-BR
Requires:       translation-update-pt_BR
Requires:       yast2-trans-pt_BR


%description
Brazilian Portuguese translations to Kamarada


%prep
cp -a %{SOURCE0} COPYING


%build


%install
files_to_add=""
files_to_add="$files_to_add /usr/lib/firefox/browser/extensions/langpack-pt-BR@firefox.mozilla.org/"
files_to_add="$files_to_add /usr/lib/firefox/browser/extensions/langpack-pt-PT@firefox.mozilla.org/"

echo "%defattr(-,root,root)" > files.kamarada-translations-ptbr
echo "%doc COPYING" >> files.kamarada-translations-ptbr

for f in $files_to_add; do
  if ! test -L "$f" && test -d "$f"; then
    mkdir -p $RPM_BUILD_ROOT/$f
    cp -R "$f/" "$RPM_BUILD_ROOT/$f/../"
  else
    mkdir -p $RPM_BUILD_ROOT/`dirname "$f"`
    cp -a "$f" "$RPM_BUILD_ROOT/$f"
  fi
  echo "$f" >> files.kamarada-translations-ptbr
done


%files -f files.kamarada-translations-ptbr


%changelog
* Wed Sep 03 2014 kamaradalinux@gmail.com
- Initial draft
