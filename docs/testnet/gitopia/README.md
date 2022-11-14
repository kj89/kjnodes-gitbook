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

**live-peers** (34)
```
peers="4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,5ed24b6ace024919dc5035a7e650af0e5a2166d5@144.76.97.251:38816,4e4f87cfa1993f4f3f7645c41f469987cafdf960@85.10.202.135:12656,bf16e96a383f317bdc40cdebfdf2a40a7b3d5c9a@142.132.166.131:26656,eec3daeed105dcd5647d1fc24ef8f1d0f404f2fe@167.235.21.149:29656,812ac9e6b05d1b610613429277e5fef4da735753@46.228.199.8:26656,7ecbed6c667415adc67648efe3b56e0bfafca532@217.79.187.96:26656,f786d8722a3f5b7dcc45714d0fc39ed088d6e2c5@94.250.203.3:6656,ff6201a652a4c1ee7c3991bb6fc1b8885eb9f357@89.163.152.83:26256,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,7e0534cc92832ce8b499ffc662a9b73d2c0351a6@135.181.162.138:27001,15bb9edc16710d321163e7ef8b9a44959dd7e657@65.108.126.46:30656,212f50ece90eb53b95b0115600bea233e0c5bec1@65.108.124.54:34656,b8cd2397920784facf0bb6cd4e30bb477f45124f@167.86.68.204:36656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,b7a2ef504e66b006ff29857fd85f1da4a40716d2@5.161.78.112:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656,5191b57c1bd202df86b67b9c7538efcf9e5c0c2a@135.181.89.99:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,9954c801a7019c5e4d7d762d4877866f7fd2a44e@176.9.106.43:36656,dbea2239b43c9e45913c22ad091abb8aaf7db469@75.119.159.159:33656,0ae35c02d8b76de9e8af1ec27df2aa446485c774@167.86.94.71:26656,db5f2aeda7308f395b7e32a65aec7b8b23a6817f@95.216.161.242:19656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,54756019bbc900b882b302786222978928d96d9e@65.109.65.210:41656,e704537ce1348bfc7b781d6546ae272ff3eea8d5@34.117.96.202:26656,6e96c0de6e437708158243153be68496d5a50119@38.242.155.23:26656,527c0753c83a5a89f5b51f50151b51a0d8638f7e@113.30.189.23:26656,875ba943654b8330d976ec97b5fcc8b9249bdf91@95.216.211.195:26656,5c08a5f53bf1984dcb5e2a461027c8f847302c9c@80.79.5.162:26656,ff49533061cca9b6c649693dba4e4c4769fa1f9f@95.216.7.169:60756,4570f274ac45e9ab114d5a467e18fa29a305b25f@135.181.1.109:41656,26da35392bb852b97beadd8339e247ba298d285d@65.108.252.216:56656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
