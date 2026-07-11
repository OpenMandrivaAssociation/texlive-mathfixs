%global tl_name mathfixs
%global tl_revision 78635

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.1
Release:	%{tl_revision}.1
Summary:	Fix various layout issues in math mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathfixs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfixs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfixs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfixs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX2e package to fix some odd behaviour in math mode such as
spacing around fractions and roots, math symbols within bold text as
well as capital Greek letters. It also adds some related macros.

