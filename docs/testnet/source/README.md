# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:12890

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:12856
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (10)
```bash
peers="a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,c5eccf228a25f979592297311bfe2cc8ef94e482@95.111.229.159:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,b57b9573b55c57c534cdb70a53138dec739b519d@212.23.222.220:26356,f6e7cb4ee4d608822802f58c85e93a7e34ce440d@65.108.237.232:28656,67958f716999fdc47fac777f0605a1911653ae86@65.109.48.181:30656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
