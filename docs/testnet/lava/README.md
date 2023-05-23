# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.11.2 | **Wasm**: OFF

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
peers="5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,122d58154d797c90323bb5424015136275bd98bf@135.181.90.135:26656,38093a87129f828125be65e8969bb7ede682b26c@38.242.197.134:26656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,71f6af45c867266f81d81193013fcb4137351355@194.163.155.84:56656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
