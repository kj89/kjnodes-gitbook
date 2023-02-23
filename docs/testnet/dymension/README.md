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
peers="747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,7c5507fbb33f846c0d8860ca80833a4d6602360a@185.197.251.5:46656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,6b00d8b9ad49cc2aa8d76416613bbbb10e6f56f7@65.109.108.150:26656,258018061069908a045d3777a7a2079588d712cf@38.242.234.6:26656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,140d07c40c964eb063d4526561ca92e8ed796b9b@65.109.82.249:29656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
