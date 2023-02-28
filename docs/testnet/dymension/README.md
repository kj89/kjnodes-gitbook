# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)




## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: [https://dymension-testnet.grpc.kjnodes.com](https://dymension-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (10)
```bash
peers="77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,488a1665d94f257733b04f7b4fbcef058cbb11cd@65.108.199.206:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@138.197.153.254:26603,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
