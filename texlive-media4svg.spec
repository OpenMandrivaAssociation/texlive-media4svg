Name:		texlive-media4svg
Version:	64686
Release:	2
Summary:	Multimedia inclusion for the dvisvgm backend
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/media4svg
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/media4svg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/media4svg.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements an interface for embedding video and
audio files in SVG (Scalable Vector Graphics) output. SVG with
embedded media is very portable, as it is supported by all
modern Web browsers across a variety of operating systems and
platforms, including portable devices. All DVI producing TeX
engines can be used. The dvisvgm utility, which is part of all
major TeX distributions, converts the intermediate DVI to SVG.
By default, media files are embedded into the SVG output to
make self-sufficient SVG files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/media4svg
%doc %{_texmfdistdir}/doc/latex/media4svg

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
