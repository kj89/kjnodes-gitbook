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

**live-peers** (30)
```bash
peers="3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,27752331150b966e3082e8dd8b364693379c1129@212.41.9.98:47656,8f009df7a9394c19c0aa3a84f129baacb66b7009@82.208.21.242:26656,7002fb6369cd13f8aa1520fd7a81e67a9adf2636@185.119.196.39:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,67794c8e6111f4356fdd7f7544e32e32a06b84de@194.146.13.180:26646,072d0711ba6a6985f4844f242bee6b598da1b90a@64.226.75.165:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,32e94653d765d9a43eb9c7a97d752dd96b2a50d6@213.247.154.10:26656,a39aac2e81ec23b639c5ed86273fcf80701187a7@5.182.36.198:46656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
