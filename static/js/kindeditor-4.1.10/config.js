/**
 * Created by Administrator on 2016/8/10.
 */
KindEditor.ready(function (K) {
    K.create('textarea[name=content]', {
        width: '800px',
        height: '200px',
        uploadJson: '/admin/upload/kindeditor',
    })
})