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

**live-peers** (11)
```bash
peers="d8b1bcfc123e63b24d0ebf86ab674a0fc5cb3b06@51.159.97.212:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,e4dec3315020ac14bc82e6f4b0696d1b0f65d999@138.201.204.5:40656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,7f928378eecafe22fe1e93d9f63db181cec3f8a3@145.239.143.76:11256,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,8c4da005c8a68682402293f951449f042e6f3dbf@164.92.190.234:21456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
