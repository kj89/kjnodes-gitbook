# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (20)
```bash
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,8535e3e22e5a10e3af6507c34b4bd9859fee4128@65.21.90.137:12856,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
