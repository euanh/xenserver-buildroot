%global debug_package %{nil}

Name:           ocaml-re
Version:        1.2.1
Release:        1
Summary:        A regular expression library for OCaml
License:        LGPL
Group:          Development/Libraries
URL:            http://github.com/ocaml/ocaml-re
Source0:        http://github.com/ocaml/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml ocaml-findlib ocaml-ocamldoc
Requires:       ocaml ocaml-findlib

%description
A regular expression library for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -install


%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc LICENSE README CHANGES
%{_libdir}/ocaml/re/*

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.1-1
- Initial package

