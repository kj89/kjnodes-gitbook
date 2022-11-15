# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (31)
```
peers="bf16e96a383f317bdc40cdebfdf2a40a7b3d5c9a@142.132.166.131:26656,4e4f87cfa1993f4f3f7645c41f469987cafdf960@85.10.202.135:12656,5ed24b6ace024919dc5035a7e650af0e5a2166d5@144.76.97.251:38816,12f6b84a23b054a6591c647c2a4456c40af65cce@5.9.147.22:24656,6a7ba7eca935a76e02b5bbb9caf149a41da9af12@144.76.27.79:46656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,9954c801a7019c5e4d7d762d4877866f7fd2a44e@176.9.106.43:36656,7761efa2f40717a8f557bba48d6e5458d167be1c@95.217.224.252:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,669e77fe3452f7b25d9cb1e95696419f0d3481da@65.109.49.163:37656,483003c31c10e10957d79b19e7da49aae225159e@65.108.152.201:26656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,64719020049e4eca90332bf77ba42443e2963ef9@65.21.248.203:22656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0534cc92832ce8b499ffc662a9b73d2c0351a6@135.181.162.138:27001,15bb9edc16710d321163e7ef8b9a44959dd7e657@65.108.126.46:30656,653f801ff91cfa9ef9595e0d96cf4ee24827e9d8@65.108.229.225:34656,3511b4bffe4d804065181625b32e2507934fdb05@82.208.20.137:26656,df5b61e51ab2f6c3bf1f3c387ba1586a84b41b25@141.95.65.26:27956,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,43edb5ddb2085727d6f6c9d0b8d6f3e4e62bf2bf@135.181.33.68:14656,0ae35c02d8b76de9e8af1ec27df2aa446485c774@167.86.94.71:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,ff6201a652a4c1ee7c3991bb6fc1b8885eb9f357@89.163.152.83:26256,d0d5136672e327c9f59402a08d24956d81ea66e0@188.166.87.208:26656,4570f274ac45e9ab114d5a467e18fa29a305b25f@135.181.1.109:41656,875ba943654b8330d976ec97b5fcc8b9249bdf91@95.216.211.195:26656,54756019bbc900b882b302786222978928d96d9e@65.109.65.210:41656,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
