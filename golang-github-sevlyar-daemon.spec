# Run tests in check section
%bcond_without check

%global goipath         github.com/sevlyar/go-daemon
Version:                0.1.4

%global common_description %{expand:
A library for writing system daemons in golang.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        A library for writing system daemons in golang
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/kardianos/osext)

%description
%{common_description}


%package devel
Summary:       %{summary}

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.4-1
- Update to release 0.1.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.3-1
- First package for Fedora

