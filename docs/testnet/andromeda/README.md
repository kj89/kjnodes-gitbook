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
peers="f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,7f32e615c80cefdd6b229cba300ef9a94287f3f3@178.250.243.84:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,364007ac7a05036820f96e0ceaf14e53b24805be@217.76.62.71:47656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,139e89b8868aed5c5922a563ecd5002959af04ff@65.108.111.236:55716,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,fd48e41b990c9ba2cdd3e2f5adf20b8ab237b328@1.15.110.177:26656,7469fd307adba5d8e782908ee01f080f3e554c48@185.154.13.19:26656,e8f8c97c65b3e65797eca3489de7c1682e85d4df@78.25.143.46:47656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,9c04d97cdd28df85495fc99997e4eec0d43c2b47@94.130.218.86:15656,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,20373ec71cffdb678099ca411fb862537f264791@178.172.212.135:26656,ce64cd3050be198f6fe0d59cd4333b40aedcfc2f@14.241.82.87:28656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
