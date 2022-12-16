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

**live-peers** (35)
```
peers="4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,6ce7f9ea8e3019c50057f4eb2a0ed55e8eedf874@194.50.0.44:26656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,09538ba6159f454a17d76501c59e23bad6fc9d3d@85.190.246.67:26656,74268fcac969cb5a1c6b8e0da4492de047bbb1ba@173.249.38.2:656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,eac23aa96a29949a033f4f8677ed43070a4f5f04@65.109.48.19:26556,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,165c6969e40fa2ae2340d8e9fa79a14589a46406@185.193.66.202:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,e88708f6bda2af195f0ec48b9868e588ead964fb@144.91.82.239:26656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,599bb15403aae7679ba59f878ee8b9c39264fc93@185.213.25.129:60956,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
