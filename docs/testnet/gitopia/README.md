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
peers="674a5a8d8f2a0815601bed562c46c060aa8ec075@65.109.70.4:60956,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,ed9e3ea0d633fa27690f5d4db039403bbb1aeba8@165.22.214.209:26656,e704537ce1348bfc7b781d6546ae272ff3eea8d5@34.117.96.202:26656,921d59eac5df9831f7a01cc120f2f550bbbf74ea@65.21.121.101:60956,d2aa45ac84cf4136182f8012b974c3e1ba762eda@65.109.53.60:56656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,6a7ba7eca935a76e02b5bbb9caf149a41da9af12@144.76.27.79:46656,e87b6771feff9f3c41e23a7c1e42b507345505fb@194.34.232.99:26656,b7a2ef504e66b006ff29857fd85f1da4a40716d2@5.161.78.112:26656,d491c840bb653847c3ec7b36a3c4493eb8da5be3@167.86.74.218:27656,d82bf877378f15e026fd10abb1a6879df55ed955@188.34.167.80:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,8072de682623fe0d0234b5722cd07b01e8ff1b49@159.65.195.169:26656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,f6eeb6fa84ec13380f420af84fc293d00ad614ad@185.202.223.189:41656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,76895e84873db23aa366296acc6900e1dd980f43@195.201.237.185:22656,e8799d0034f6b99cc01916639dc424c7d2548784@185.169.252.60:36656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,4fcd7fd0a9585f3ddc547ec7204b2bbafa35f2f2@185.92.148.124:36656,686e8d4b842a91cf63170de500d5351f49b440ce@206.189.0.110:26656,d2291c87bdef89c31f8e4008ddc0dee2d2a8ef50@143.244.182.43:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
