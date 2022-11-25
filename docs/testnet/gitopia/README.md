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
peers="fdeb051aae6f555150bb4cf685719879f21cd3e4@217.13.223.167:36656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,12f6b84a23b054a6591c647c2a4456c40af65cce@5.9.147.22:24656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,54157f773b7135a134b1953d8c8a0ff128cad2f5@194.233.68.165:41656,212f50ece90eb53b95b0115600bea233e0c5bec1@65.108.124.54:34656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,8a86d39f08c47ed0ef2bd21606f16817744a3742@38.242.203.117:26656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,7a1c9ad925788a1811340b88068d6750c4511714@194.163.140.239:41656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,d2291c87bdef89c31f8e4008ddc0dee2d2a8ef50@143.244.182.43:26656,d491c840bb653847c3ec7b36a3c4493eb8da5be3@167.86.74.218:27656,e572ad8a5c190a82c0a68905c76cd7d61d22b578@161.35.39.251:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
