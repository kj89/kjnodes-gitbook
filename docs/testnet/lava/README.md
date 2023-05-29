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
peers="1fd86f6ba06ef4b189276f97f70fea04161019db@144.76.176.154:11656,5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,3f6d9698d9a5d9fe17afa5968ea652fae478b32f@185.250.37.239:32656,ba78f0ac713d5e7a0274ef593674dae337aabbee@176.103.222.18:26656,1dc8db6b9b800deded531bfb56ce12defbc98c74@173.249.46.50:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,1a18bdd0c259d604cda023a5e03eba2a25f5c045@94.19.249.187:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
