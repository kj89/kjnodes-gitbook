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

**live-peers** (10)
```bash
peers="57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,82b51653205df40d43f257041db2da0f9f1644fa@178.63.26.94:46656,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,7f928378eecafe22fe1e93d9f63db181cec3f8a3@145.239.143.76:11256,b989bcba871776cf50d39c2e58763677dc082181@45.14.194.130:26656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,3fdba29b1d02066f6406c611e1ae42e9ec76bbf2@185.197.194.227:26656,0d7ec1ea841e763267f197e2e0aa89467da24064@94.19.249.187:35656,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
