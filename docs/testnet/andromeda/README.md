# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (9)
```bash
peers="69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,1c101b595362f6a5856ef34f43545cf95eb34912@65.109.26.21:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,b3bb0cc43425abb61a26fe96a0c543f7a77416d6@135.181.217.182:15656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
