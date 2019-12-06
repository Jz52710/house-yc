<template>
    <div class="index">
        <el-row :span="24" style="margin: 0 auto;">
            <el-col :span="12" style="margin: 20px auto;background: lightcyan;padding: 20px;position: absolute;left: 0;right: 0;">
                <h2>房价预测</h2>
                <el-form ref="form" :model="form" label-width="80px" >
                    <el-form-item label="城市">
                        <el-select v-model="form.city" placeholder="请选择城市">
                            <el-option label="北京" value="0"></el-option>
                            <el-option label="上海" value="1"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="城区">
                        <el-select v-model="form.proper" placeholder="请选择城区">
                            <el-option label="朝阳区" value="1"></el-option>
                            <el-option label="东城区" value="1"></el-option>
                            <el-option label="丰台区" value="1"></el-option>
                            <el-option label="海淀区" value="1"></el-option>
                            <el-option label="昌平区" value="1"></el-option>
                            <el-option label="西城区" value="1"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="房间">
                        <el-select v-model="form.roomnum" placeholder="请选择房间">
                            <el-option label="一室" value="1"></el-option>
                            <el-option label="两室" value="2"></el-option>
                            <el-option label="三室" value="3"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="大厅">
                        <el-select v-model="form.halls" placeholder="请选择客厅">
                            <el-option label="一厅" value="1"></el-option>
                            <el-option label="两厅" value="2"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="面积">
                        <el-col style="width:221px;margin-left: 212px">
                            <el-input v-model="form.area" placeholder="请输入面积"></el-input>
                        </el-col>
                    </el-form-item>
                    <el-form-item label="楼层">
                        <el-select v-model="form.floors" placeholder="请选择楼层">
                            <el-option label="低层" value="0"></el-option>
                            <el-option label="中层" value="1"></el-option>
                            <el-option label="高层" value="1"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="靠近地铁">
                        <el-radio-group v-model="form.subway">
                            <el-radio label="是"></el-radio>
                            <el-radio label="否"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item label="靠近学校">
                        <el-radio-group v-model="form.school">
                            <el-radio label="是"></el-radio>
                            <el-radio label="否"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">立即创建</el-button>
                    </el-form-item>
                </el-form>
            </el-col>
        </el-row>
    </div>
</template>
<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'home',
        components: {
            // HelloWorld
        },
        data() {
            return {
                form: {
                    city:'',
                    area:'',
                    subway:'',
                    roomnum:'',
                    halls:'',
                    proper:'',
                    floors:'',
                    school:''
                }
            }
        },
        methods: {
            onSubmit() {
                let data = {'city':this.form.city,'proper':this.form.proper,'roomnum':this.form.roomnum,'halls':this.form.halls,'area':this.form.area,'floors':this.form.floors,'subway':this.form.subway,'school':this.form.school};
                 this.$axios.post('/api/price',data).then((res)=>{
                    // this.$message.success('已添加到想看');
                     alert('该地区的房价为：'+res.data.data)
                }).catch(function (error) {
                    alert(error)
                });
            }
        }
    }
</script>

