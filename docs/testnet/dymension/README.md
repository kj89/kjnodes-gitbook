# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (9)
```bash
peers="7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,f4be55edab4b5cb40464aa50def5d2cd39359e67@185.182.185.101:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
