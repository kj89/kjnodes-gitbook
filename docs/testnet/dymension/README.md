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
peers="7b4621b7744a2c3ea5ec9453980e1d555109a746@139.162.138.158:26656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,e1d6bdf47f76bdfdba90d4bedc780539d9766bbe@172.104.199.176:26656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
