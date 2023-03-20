# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,50ce639d8889108b488f0aa802468bc13d4873a4@75.119.159.195:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,6006190d5a3a9686bbcce26abc79c7f3f868f43a@37.252.184.230:26656,3c5024a2213f8bae01e85f450e3d5eb11cf28768@95.217.188.65:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,d78df88bc4a487c140e466a23f549ed90e7ebfb6@161.97.152.157:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
