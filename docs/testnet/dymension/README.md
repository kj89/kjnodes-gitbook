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
peers="7b4621b7744a2c3ea5ec9453980e1d555109a746@139.162.138.158:26656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@138.197.153.254:26603,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,6ebe5856a7617cb9309a923a3935687903d2607d@141.95.97.28:15256,7c5507fbb33f846c0d8860ca80833a4d6602360a@185.197.251.5:46656,74cfbc9e923784d1ca73188053561ea8b09e13d4@146.190.127.9:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
