# 1. clone, pull
## 1) clon
>원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어
- `git clone <원격 저장소 주소>` 의 형태로 작성한다.
    ```bash
    $ git clone https://github.com/leeyonghee1017/TIL.git
    Cloning into 'TIL'...
    remote: Enumerating objects: 3, done.
    remote: Counting objects: 100% (3/3), done.
    remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
    Receiving objects: 100% (3/3), done.
    ```
- git clone을 통해 생성된 로컬 저장소는 `git init` 과 `git remote add` 가 이미 수행되어 있다.
## 2) pull
>원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어
- `git pull <저장소 이름> <브랜치 이름>` 의 형태로 작성한다.
    ```bash
    $ git pull origin master
    From https://github.com/leeyonghee/TIL
   * branch            master     -> FETCH_HEAD
    Updating 6570ecb..56809a9
    Fast-forward
     README.md | 1 +
    1 file changed, 1 insertion(+)


    [풀이]
    git 명령어를 사용할건데, origin이라는 원격 저장소의 master 브랜치의 내용을 가져온다(pull).
    ```

# 2. Branch
> 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구이다.
## 1) git branch
>브랜치 `조회, 생성, 삭제` 등 브랜치와 관련된 Git 명령어
```bash
# 브랜치 목록 확인
$ git branch

# 원격 저장소의 브랜치 목록 확인
$ git branch -r

# 새로운 브랜치 생성
$ git branch <브랜치 이름>

# 특정 커밋 기준으로 브랜치 생성
$ git branch <브랜치 이름> <커밋 ID>

# 특정 브랜치 삭제
$ git branch -d <브랜치 이름> # 병합된 브랜치만 삭제 가능
$ git branch -D <브랜치 이름> # (주의) 강제 삭제 (병합되지 않은 브랜치도 삭제 가능)
```
## 2) git switch
>현재 브랜치에서 다른 브랜치로 `HEAD` 를 이동시키는 명령어.
`HEAD` 란 현재 브랜치를 가리키는 포인터를 의미한다.
```bash
# 다른 브랜치로 이동
$ git switch <다른 브랜치 이름>

# 브랜치를 새로 생성과 동시에 이동
$ git switch -c <브랜치 이름>

# 특정 커밋 기준으로 브랜치 생성과 동시에 이동
$ git switch -c <브랜치 이름> <커밋 ID>
```

# 3. Branch Merge
> `브랜치를 병합` 하여 합치는 것
## 1) git merge
- 분기된 브랜치들을 하나로 합치는 명령어
- `git merge <합칠 브랜치 이름>` 의 형태로 사용한다.
- **Merge하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야한다.**
  ```bash
  # 1. 현재 branch1과 branch2가 있고, HEAD가 가리키는 곳은 branch1 이다.
    $ git branch
    * branch1
      branch2

    # 2. branch2를 branch1에 합치려면?
    $ git merge branch2

    # 3. branch1을 branch2에 합치려면?
    $ git switch branch2
    $ git merge branch1
  ```
## 2) Merge의 세 종류
- `Fast-Forward`
  - 브랜치를 병합할 때 마치 `빨리감기` 처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 것
- `3-Way Merge`
  - 브랜치를 병합할 때 `각 브랜치의 커밋 두개와 공통 조상 하나` 를 사용하여 병합하는 것
  - 두 브랜치에서 `다른 파일` 혹은 `같은 파일의 다른 부분` 을 수정했을 때 가능하다.
- `Merge Conflict`
  - 병합하는 두 브랜치에서 `같은 파일의 같은 부분` 을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못해서 발생하는 충돌(Conflict) 현상
  - 결국은 사용자가 직접 내용을 선택해서 Conflict를 해결해야 한다.

# 4. Git workflow
## 1) 원격 저장소 소유권이 있는 경우
- 원격 저장소가 자신의 소유이거나 collaborator로 등록되어 있는 경우에 가능하다.
- master에 직접 개발하는 것이 아니라, `기능별로 브랜치` 를 따로 만들어서 개발한다.
- `Pull Request` 를 같이 사용하여 팀원 간 변경 내용에 대한 소통을 진행한다.
### i. 작업 흐름
- 소유권이 있는 원격 저장소를 로컬 저장소로 clone 받는다.
    ```bash
    $ git clone https://github.com/leeyonghee1017/django-project.git
    ```
- 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성` 하고, 그 안에서 `기능을 구현` 한다.
    ```bash
    $ git switch -c feature/login
    ```
- 기능 구현이 완료되면, 원격 저장소에 해당 브랜치를 push 한다.
    ```bash
    $ git push origin feature/login
    ```
- 원격 저장소에는 master와 각 기능의 브랜치가 반영된다.
- Pull Request를 통해 브랜치를 master에 반영해달라는 요청을 보낸다.
(팀원들과 코드 리뷰를 통해 소통할 수 있다.)
- 병합이 완료되면 원격 저장소에서 병합이 완료된 브랜치는 불필요하므로 삭제한다.
- master에 브랜치가 병합되면, 각 사용자는 로컬의 master 브랜치로 이동한다.
    ```bash
    $ git switch master
    ```
- 병합으로 인해 변경된 원격 저장소의 master 내용을 로컬에 받아온다.
    ```bash
    $ git pull origin master
    ```
- 병합이 완료된 master의 내용을 받았으므로, 기존 로컬 브랜치는 삭제한다. (한 사이클 종료)
    ```bash
    $ git branch -d feature/login
    ```
- 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복한다.

## 2) 원격 저장소 소유권이 없는 경우
- 오픈 소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우 사용한다.
- 원본 원격 저장소를 그대로 내 원격 저장소에 `복제` 한다. (이 행위를 `fork` 라고 합니다.)
- 기능 완성 후 `Push는 복제한 내 원격 저장소에 진행` 한다.
- 이후 `Pull Request` 를 통해 원본 원격 저장소에 반영될 수 있도록 요청한다.

### i. 작업 흐름
- 소유권이 없는 원격 저장소를 `fork` 를 통해 내 원격 저장소로 `복제` 한다.
    ![fork](image/fork.png)
- `fork` 후, 복제된 내 원격 저장소를 로컬 저장소에 `clone` 받는다.
    ```bash
    $ git clone https://github.com/leeyonghee1017/kakao_clone.git
    ```
- 이후에 로컬 저장소와 원본 원격 저장소를 동기화 하기 위해서 연결한다.
    ```bash
    # 원본 원격 저장소에 대한 이름은 upstream으로 붙이는 것이 일종의 관례

    $ git remote add upstream https://github.com/AlexKwonPro/kakao_clone.git
    ```
- 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성` 하고, 그 안에서 `기능을 구현` 한다.
    ```bash
    $ git switch -c feature/login
    ```
- 기능 구현이 완료되면, `복제 원격 저장소(origin)` 에 해당 브랜치를 `push` 한다.
    ```bash
    $ git push origin feature/login
    ```
- `복제 원격 저장소(origin)` 에는 master와 브랜치가 반영되었다.
- `Pull Request` 를 통해 `복제 원격 저장소(origin)의 브랜치` 를 `원본 원격 저장소(upstream)의 master` 에 반영해달라는 요청을 보낸다. 
(원본 원격 저장소의 관리자가 코드 리뷰를 진행하여 반영 여부를 결정한다.)
- `원본 원격 저장소(upstream)` 의 master에 브랜치가 병합되면 `복제 원격 저장소(origin)` 의 브랜치는 삭제한다. 그리고 사용자는 로컬에서 master 브랜치로 이동한다.
    ```bash
    $ git switch master
    ```
- 병합으로 인해 변경된 `원본 원격 저장소(upstream)의 master`  내용을 로컬에 받아온다. 
그리고 기존 로컬 브랜치는 삭제한다. (한 사이클 종료)
    ```bash
    $ git pull upstream master
    $ git branch -d feature/login
    ```
- 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복한다.
    ```bah
    $ git switch -c feature/pay
    ```