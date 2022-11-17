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

**live-peers** (26)
```
peers="56c544dc2cf49daddc5958976ba01b8719a06200@65.21.178.237:656,cdc40dd0b56a9b58a155856a99fee3ff8c037076@65.21.196.153:46656,921d59eac5df9831f7a01cc120f2f550bbbf74ea@65.21.121.101:60956,9954c801a7019c5e4d7d762d4877866f7fd2a44e@176.9.106.43:36656,334581d5ec3b87a01623f2ac70f3eeb9012cb60b@68.183.71.8:26656,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,bb6f0d3c55a6834037d545159869388bc498a5c7@144.76.90.130:27656,3511b4bffe4d804065181625b32e2507934fdb05@82.208.20.137:26656,98a1522fc5c2c200f8363ba5885771e7ec1ab5c7@95.217.211.32:26656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,2872a520d0d04bc2a3df260ab04d983dd034174f@65.109.85.215:60956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,d3fb1c74c2b38a220e113d450afd3000922e5eff@65.109.84.216:60956,6a60ce141f8e9055609c56f214a5f10f7bef67e0@154.26.138.224:41656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,0cccef180d7597bbeef7d2b80d52913ab205879f@65.108.193.133:26656,fbd3b296871ae841b638158e29d48e09180b7c4e@194.233.77.238:41656,e87b6771feff9f3c41e23a7c1e42b507345505fb@194.34.232.99:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,a4eefa82608b31b55b70307f3db0d88261d8ed9b@154.53.57.72:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
