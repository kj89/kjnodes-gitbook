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
peers="5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,da23ed57fc3d03b3864c309b589f2b5130a04a9f@65.109.111.204:28656,67958f716999fdc47fac777f0605a1911653ae86@65.109.48.181:30656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,86216a2e88322ca534fedaa91898272cc11d3cc9@173.249.23.196:28656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
