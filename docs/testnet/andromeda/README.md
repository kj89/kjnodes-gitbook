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

**live-peers** (12)
```bash
peers="4d4ef8f6ff2f1ac8ba5e102e858f6ecbd0d3dda1@31.220.84.3:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,a583f951655a3c9934944d332bb4f6cf7416a3b7@94.131.108.126:26656,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
