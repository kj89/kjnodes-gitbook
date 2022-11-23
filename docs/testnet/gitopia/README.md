# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (24)
```
peers="f06f794dcc5964197da0e13709d71ea5e0f5b7f1@88.99.3.158:11156,d312ba9da73e07c88918c56908e84ba28907808a@65.108.69.68:26858,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,a47375da7f790427c69103d363e4f8de4a6acfac@5.199.143.159:36656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,05fa81c618612d6730cb8b54620954ce384899af@146.190.218.191:41656,a536f71fcc2497cc7f8ef2b74b43368eaf3bf1b8@65.109.51.41:60956,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,75a9570b82474af11fc8c895f9da1ecb5da0c73f@95.216.143.237:19656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,e53572d91ae5c25caf23b6390467d1d2978ae3b7@65.109.14.17:26656,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,483003c31c10e10957d79b19e7da49aae225159e@65.108.152.201:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,d2aa45ac84cf4136182f8012b974c3e1ba762eda@65.109.53.60:56656,653f801ff91cfa9ef9595e0d96cf4ee24827e9d8@65.108.229.225:34656,45cc764ce4547208c21f62340a280cff1f2a4ab5@5.9.147.185:26156,98a1522fc5c2c200f8363ba5885771e7ec1ab5c7@95.217.211.32:26656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,b79965e5cf163ca68d6720f6e9db2c18ea9f5810@72.14.185.165:26656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
