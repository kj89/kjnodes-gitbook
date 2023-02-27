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
peers="7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,cffb2a5e8fe08ba5ce46a8f56a4a1cdf636cbf8e@5.231.205.142:26656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
