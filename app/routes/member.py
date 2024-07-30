from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터 생성
member_router = APIRouter()
# 탬플릿 지정
templetes = Jinja2Templates(directory='views/templates')

@member_router.get("/login", response_class=HTMLResponse)
async def login(req: Request):
    return templetes.TemplateResponse('member/login.html', {'request': req})

@member_router.get("/join", response_class=HTMLResponse)
async def join(req: Request):
    return templetes.TemplateResponse('member/join.html', {'request': req})

@member_router.get("/myinfo", response_class=HTMLResponse)
async def myinfo(req: Request):
    return templetes.TemplateResponse('member/myinfo.html', {'request': req})
