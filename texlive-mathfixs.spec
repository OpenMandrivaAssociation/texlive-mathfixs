Name:		texlive-mathfixs
Version:	72653
Release:	1
Summary:	Fix various layout issues in math mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathfixs
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfixs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfixs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfixs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX2e package to fix some odd behaviour in math
mode such as spacing around fractions and roots, math symbols
within bold text as well as capital Greek letters. It also adds
some related macros.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mathfixs
%{_texmfdistdir}/tex/latex/mathfixs
%doc %{_texmfdistdir}/doc/latex/mathfixs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
