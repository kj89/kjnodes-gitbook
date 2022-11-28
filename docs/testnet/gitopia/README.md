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

**live-peers** (29)
```
peers="f91f270980654a74c7619eff18bc068d2b86e6d8@54.90.149.14:41656,e8799d0034f6b99cc01916639dc424c7d2548784@185.169.252.60:36656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,d3fb1c74c2b38a220e113d450afd3000922e5eff@65.109.84.216:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,e693197ec64ff270fbee9c5b9d8d055ec6fff1cb@65.21.121.101:46656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,5b84bcb89128bd8fd8d5619dffbd2b6e460cd857@65.21.58.131:26656,c630e7695e89074bf25a49afac7aca33feca9fd2@95.217.216.88:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,09538ba6159f454a17d76501c59e23bad6fc9d3d@85.190.246.67:26656,ed9e3ea0d633fa27690f5d4db039403bbb1aeba8@165.22.214.209:26656,54157f773b7135a134b1953d8c8a0ff128cad2f5@194.233.68.165:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,eec3daeed105dcd5647d1fc24ef8f1d0f404f2fe@167.235.21.149:29656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,7ecbed6c667415adc67648efe3b56e0bfafca532@217.79.187.96:26656,62c6caafd89eaa885157fc6311b345064f6b1468@185.213.25.129:60956,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,ebbd018513778be2d77f3495fa7da722116ad64f@194.146.13.128:60956,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,61af145c3cf74b80f2a7187a55499a3c97e35a8e@38.242.130.204:41656,f786d8722a3f5b7dcc45714d0fc39ed088d6e2c5@94.250.203.3:6656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
