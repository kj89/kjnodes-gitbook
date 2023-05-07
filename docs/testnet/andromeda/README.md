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

**live-peers** (10)
```bash
peers="d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,63bfe9e8b52ed6b7472a120559f3c4a61b7e0a80@65.109.82.154:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
