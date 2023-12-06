import openai
import streamlit as st

# gpt에게 글 요청
def askGPT(prompt,apiKey):
    client = openai.OpenAI(api_key=apiKey)
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {'role':'user','content':prompt}
        ]
    )
    finalResponse = response.choices[0].message.content
    return finalResponse

# main 함수
def main():
    st.set_page_config(page_title='광고문구 생성 프로그램')

    # session_state 초기화
    if 'OPENAI_API' not in st.session_state:
        st.session_state['OPENAI_API'] = ''

    with st.sidebar:
        openai_apiKey = st.text_input(label='OPEN API 키',placeholder='Enter your api key')

        if openai_apiKey:
            st.session_state['OPENAI_API'] = openai_apiKey
        st.markdown('----')

    st.header(':rainbow: 광고문구 생성 프로그램 :tangerine:')
    st.markdown('----')

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input('제품명',placeholder='')
        strength = st.text_input('제품 특징',placeholder='')
        keywords = st.text_input('필수 포함 키워드',placeholder='')

    with col2:
        brand = st.text_input('브랜드명', placeholder= '애플,''올리브영, ...')
        tonNman = st.text_input('톤앤매너', placeholder= '유머러스하게'',감성적으로 ,...')
        value = st.text_input('브랜드 핵심 가치',placeholder= '필요시 작성')

    # text = st.text_area('생성할 글을 입력하세요.')
    if st.button('광고 문구 생성'):
        prompt = f'''
        **Please refer to the following information and provide five short advertising phrases (1-2 lines each) with the following details.** :
        - Product name: {name}
        - Brand name: {brand}
        - Core values of the brand: {strength}
        - Product features: {tonNman}
        - Essential keywords to include: {keywords}
    '''
        st.info(askGPT(prompt,st.session_state['OPENAI_API']))

if __name__ == '__main__':     ## __main()__ 이 페이지 만들때 기계가 읽는 시작점이니까 꼭 넣어줘. 중요해 이거!
    main()