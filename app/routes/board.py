from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터 생성
board_router = APIRouter()
# 탬플릿 지정
templetes = Jinja2Templates(directory='views/templates')

@board_router.get("/write", response_class=HTMLResponse)
async def write(req: Request):
    return templetes.TemplateResponse('board/write.html', {'request': req})

@board_router.get("/list", response_class=HTMLResponse)
async def list(req: Request):
    return templetes.TemplateResponse('board/list.html', {'request': req})

@board_router.get("/view", response_class=HTMLResponse)
async def view(req: Request):
    return templetes.TemplateResponse('board/view.html', {'request': req})

@board_router.get("/remove", response_class=HTMLResponse)
async def romove(req: Request):
    return templetes.TemplateResponse('board/list.html', {'request': req})

@board_router.get("/modify", response_class=HTMLResponse)
async def modify(req: Request):
    return templetes.TemplateResponse('board/modify.html', {'request': req})
