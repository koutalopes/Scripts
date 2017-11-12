" URL: http://vim.wikia.com/wiki/Example_vimrc
" Authors: http://vim.wikia.com/wiki/Vim_on_Freenode
" Description: A minimal, but feature rich, example .vimrc. If you are a
"              newbie, basing your first .vimrc on this file is a good choice.
"              If you're a more advanced user, building your own .vimrc based
"              on this file is still a good idea.
"------------------------------------------------------------
set nocompatible
filetype indent plugin on
syntax on
set backspace=indent,eol,start
set autoindent
set number
set shiftwidth=4
set softtabstop=4
set expandtab
set visualbell
"------------------------------------------------------------
" plugins (managed by https://github.com/junegunn/vim-plug)
call plug#begin('~/.local/share/nvim/plugged')

" airline (powerline) - https://github.com/vim-airline/vim-airline
Plug 'vim-airline/vim-airline'

" airline themes - https://github.com/vim-airline/vim-airline-themes
Plug 'vim-airline/vim-airline-themes'

" github wrapper - https://github.com/tpope/vim-fugitive
Plug 'tpope/vim-fugitive'

" deoplete (autocompletion) - https://github.com/Shougo/deoplete.nvim
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }

Plug 'jiangmiao/auto-pairs'

" deoplete completions sources
Plug 'https://github.com/zchee/deoplete-clang.git'
Plug 'https://github.com/Shougo/neco-syntax.git'
Plug 'https://github.com/zchee/deoplete-jedi.git'
call plug#end()
"------------------------------------------------------------
" set powerline patched fonts on vim-airline
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
" set theme for airline
let g:airline_theme = 'minimalist'
" -----------------------------------------------------------
let g:deoplete#enable_at_startup = 1 "start deoplete
let g:deoplete#sources#clang#libclang_path = '/usr/lib/libclang.so' "path to libclang.so
let g:deoplete#sources#clang#clang_header = '/usr/lib64/clang' "path to clang header directory
autocmd CompleteDone * silent! pclose!
let $NVIM_TUI_ENABLE_TRUE_COLOR = 1
