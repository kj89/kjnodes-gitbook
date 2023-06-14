# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.13.1 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:14490

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:14456
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:14459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (10)
```bash
peers="e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,b294ab07592bb93a85b099fb684dd96a98e12ba9@178.63.102.172:23356,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,f22ea1e7b6d31966259e99177d714cffde27c4bf@152.32.211.182:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,125935f63c123b6891b014ffc071fbf781270771@23.88.74.54:11656,1550fe479ee2dcfa35f7dcd2c66f37a50d34b0e3@178.63.132.243:2237,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
