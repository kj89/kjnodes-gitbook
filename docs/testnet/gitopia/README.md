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
peers="8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,75a9570b82474af11fc8c895f9da1ecb5da0c73f@95.216.143.237:19656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,ae5d5b47ea732ff509114f405967f61eb3d86ac6@75.119.146.171:656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,165c6969e40fa2ae2340d8e9fa79a14589a46406@185.193.66.202:26656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,74268fcac969cb5a1c6b8e0da4492de047bbb1ba@173.249.38.2:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,44a66336b029ba931165da3580cc6322af90339d@38.242.207.87:26656,7f2339fc6a6dca666d8ffbbe4e61443d58e0e759@109.123.255.8:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
