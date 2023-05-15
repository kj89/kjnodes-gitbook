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
peers="37add870e1f40b6b00a55b71d20590b2128fdd3d@88.99.33.248:26656,b16eb3c538b9a460612a4cea37c2657f15579126@65.109.30.90:11656,ca1c561ad051d12cf99d8846303f4d31bfe3eb83@138.197.57.142:26656,ac7cefeff026e1c616035a49f3b00c78da63c2e9@18.215.128.248:26656,147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,71f6af45c867266f81d81193013fcb4137351355@194.163.155.84:56656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,a5e61061417d9d4b51bbfa2a66042cfce7047f5d@195.201.197.4:14656,3693ea5a8a9c0590440a7d6c9a98a022ce3b2455@65.109.92.79:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
