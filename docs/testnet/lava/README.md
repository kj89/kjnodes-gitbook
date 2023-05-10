# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.10.1 | **Wasm**: OFF

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
peers="8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,21eb46c44f46820e42cfe4afbe2f1104eef95cfc@135.181.221.186:30656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,1550fe479ee2dcfa35f7dcd2c66f37a50d34b0e3@178.63.132.243:2237,71f6af45c867266f81d81193013fcb4137351355@194.163.155.84:56656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
