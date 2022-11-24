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

**live-peers** (21)
```
peers="76895e84873db23aa366296acc6900e1dd980f43@195.201.237.185:22656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,3511b4bffe4d804065181625b32e2507934fdb05@82.208.20.137:26656,fdeb051aae6f555150bb4cf685719879f21cd3e4@217.13.223.167:36656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,54157f773b7135a134b1953d8c8a0ff128cad2f5@194.233.68.165:41656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,8072de682623fe0d0234b5722cd07b01e8ff1b49@159.65.195.169:26656,fbd3b296871ae841b638158e29d48e09180b7c4e@194.233.77.238:41656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,2236a75a7557d8633d06ac6f036c1b47c1fd1598@149.102.158.166:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,bfe5342ae808946452ed1ff21f5cb69f4f4bf78b@38.242.250.242:26656,b79965e5cf163ca68d6720f6e9db2c18ea9f5810@72.14.185.165:26656,65cf46c1f9fbab6ec70cd295c9391abdedc1b17c@139.59.177.5:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
