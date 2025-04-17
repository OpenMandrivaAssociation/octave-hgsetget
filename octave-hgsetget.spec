%global octpkg hgsetget

Summary:	Matlab-compatible superclass used to derive handle class with set and get metho
Name:		octave-hgsetget
Version:	0.1
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/hgsetget/
Url:		https://gitlab.com/farhi/octave-hgsetget/
Source0:	https://gitlab.com/farhi/octave-hgsetget/-/archive/%{version}/octave-hgsetget-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Matlab-compatible superclass used to derive handle class with set and 
get methods.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

