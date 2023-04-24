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

**live-peers** (29)
```bash
peers="7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,13eff3f60e60546435a9f79e241372b299f559a1@5.161.80.223:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,acd9b98fcd66c9ce0300607d08e0811683638b97@194.163.132.27:34656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,6aaf94803e3f387a3ee08b731890e6914e1e3419@65.108.233.102:30656,e8f8c97c65b3e65797eca3489de7c1682e85d4df@78.25.143.46:47656,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,de8e1fd6c53fa464965b547d100f091277ddcb04@80.89.229.115:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,011c1c98fb63b99e8fd2aaf8a02f60cd45154179@45.132.106.178:26656,7469fd307adba5d8e782908ee01f080f3e554c48@185.154.13.19:26656,a39aac2e81ec23b639c5ed86273fcf80701187a7@5.182.36.198:26656,699ca7c3496f2c3f2cf476f51c6e6420d4c20fc1@23.121.249.57:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,7ba9cadf6197c30fa808d9315333054ef953be9c@144.76.164.139:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
