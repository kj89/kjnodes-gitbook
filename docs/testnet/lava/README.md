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
peers="5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,2a588e5ddcfd8c9095cc6f34b5b6966e31020cfd@65.21.123.172:11656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,e1c09e10296de98d5637e0f948ada9d477ad4d75@31.42.191.74:36656,21eb46c44f46820e42cfe4afbe2f1104eef95cfc@135.181.221.186:30656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
