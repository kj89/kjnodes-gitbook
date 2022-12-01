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

**live-peers** (32)
```
peers="986afccee8c833afc2917075418474c1e9bf9fcb@65.109.82.75:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,51c3b05112f73a6e60e8b2e96d5528a39a3f4e5e@38.242.246.96:26656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,0d4c392f44c081347775643d99311bf2b36a7377@80.241.220.27:60956,c6dcaf5c1d59c696a5b93f53cc5a855b2399f09c@149.102.146.49:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,33196fb0090d2de3671e36545d3425f641c9c0dc@65.109.70.4:41656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,fe7af0c284fac131aa66448fafcc89e7f8298274@49.12.33.189:26656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,f91f270980654a74c7619eff18bc068d2b86e6d8@54.90.149.14:41656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,101c8fd5e3714c8d371de8c130a84032a3811c3c@95.217.211.135:13656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,f06f794dcc5964197da0e13709d71ea5e0f5b7f1@88.99.3.158:11156,965e495f4a69294bd85f3437fccdc9b210fd98b6@1.15.146.92:26656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
