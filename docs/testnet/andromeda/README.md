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

**live-peers** (17)
```bash
peers="8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,35d1047d50226c8dd42f2402c212f92bf7935108@65.109.112.20:11164,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
