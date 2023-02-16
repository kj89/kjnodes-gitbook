# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: [https://rebus.grpc.kjnodes.com](https://rebus.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
